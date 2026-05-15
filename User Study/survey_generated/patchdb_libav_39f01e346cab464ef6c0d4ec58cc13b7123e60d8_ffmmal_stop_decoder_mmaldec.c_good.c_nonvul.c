static void ffmmal_stop_decoder(AVCodecContext *avctx)
{
    MMALDecodeContext *ctx = avctx->priv_data;
    MMAL_COMPONENT_T *decoder = ctx->decoder;
    MMAL_BUFFER_HEADER_T *buffer;
    mmal_port_disable(decoder->input[0]);
    mmal_port_disable(decoder->output[0]);
    mmal_port_disable(decoder->control);
    mmal_port_flush(decoder->input[0]);
    mmal_port_flush(decoder->output[0]);
    mmal_port_flush(decoder->control);
    while ((buffer = mmal_queue_get(ctx->queue_decoded_frames)))
        mmal_buffer_header_release(buffer);
    while (ctx->waiting_buffers)
    {
        FFBufferEntry *buffer = ctx->waiting_buffers;
        ctx->waiting_buffers = buffer->next;
        av_buffer_unref(&buffer->ref);
        av_free(buffer);
    }
    ctx->waiting_buffers_tail = NULL;
    assert(avpriv_atomic_get(&ctx->packets_buffered) == 0);
    ctx->frames_output = ctx->eos_received = ctx->eos_sent = ctx->packets_sent = ctx->extradata_sent = 0;
}