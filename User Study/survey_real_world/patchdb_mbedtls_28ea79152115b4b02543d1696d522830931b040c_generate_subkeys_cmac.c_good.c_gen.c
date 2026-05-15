static int generate_subkeys(mbedtls_cmac_context *ctx)
{
    int ret;
    unsigned char L[16];
    size_t olen;
    if ((ret = mbedtls_cipher_update(&ctx->cipher_ctx, L, 16, L, &olen)) != 0)
    {
        return (ret);
    }
    multiply_by_u(ctx->K1, L);
    multiply_by_u(ctx->K2, ctx->K1);
    mbedtls_zeroize(L, sizeof(L));
    return (0);
}