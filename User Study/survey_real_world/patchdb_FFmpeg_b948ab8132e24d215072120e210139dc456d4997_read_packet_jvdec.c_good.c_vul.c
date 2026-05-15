static int read_packet(AVFormatContext *s, AVPacket *pkt)
{
    JVDemuxContext *jv = s->priv_data;
    AVIOContext *pb = s->pb;
    AVStream *ast = s->streams[0];
    while (!url_feof(s->pb) && jv->pts < ast->nb_index_entries)
    {
        const AVIndexEntry *e = ast->index_entries + jv->pts;
        const JVFrame *jvf = jv->frames + jv->pts;
        switch (jv->state)
        {
        case JV_AUDIO:
            jv->state++;
            if (jvf->audio_size)
            {
                if (av_get_packet(s->pb, pkt, jvf->audio_size) < 0)
                    return AVERROR(ENOMEM);
                pkt->stream_index = 0;
                pkt->pts = e->timestamp;
                pkt->flags |= AV_PKT_FLAG_KEY;
                return 0;
            }
        case JV_VIDEO:
            jv->state++;
            if (jvf->video_size || jvf->palette_size)
            {
                int size = jvf->video_size + jvf->palette_size;
                if (av_new_packet(pkt, size + JV_PREAMBLE_SIZE))
                    return AVERROR(ENOMEM);
                AV_WL32(pkt->data, jvf->video_size);
                pkt->data[4] = jvf->video_type;
                if ((size = avio_read(pb, pkt->data + JV_PREAMBLE_SIZE, size)) < 0)
                    return AVERROR(EIO);
                pkt->size = size + JV_PREAMBLE_SIZE;
                pkt->stream_index = 1;
                pkt->pts = jv->pts;
                if (jvf->video_type != 1)
                    pkt->flags |= AV_PKT_FLAG_KEY;
                return 0;
            }
        case JV_PADDING:
            avio_skip(pb, FFMAX(e->size - jvf->audio_size - jvf->video_size - jvf->palette_size, 0));
            jv->state = JV_AUDIO;
            jv->pts++;
        }
    }
    if (s->pb->eof_reached)
        return AVERROR_EOF;
    return AVERROR(EIO);
}