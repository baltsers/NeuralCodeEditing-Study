void apm_cpu_idle()
{
    struct apmregs regs;
    if (!apminited || !apmidleon)
        return;
    if (apmcall(APM_CPU_IDLE, 0, &regs) != 0)
        apm_perror("set CPU idle", &regs);
}