static void rt6_free_pcpu(struct rt6_info *non_pcpu_rt)
{
    int cpu;
    if (!non_pcpu_rt->rt6i_pcpu)
        return;
    for_each_possible_cpu(cpu)
    {
        struct rt6_info **ppcpu_rt;
        struct rt6_info *pcpu_rt;
        ppcpu_rt = per_cpu_ptr(non_pcpu_rt->rt6i_pcpu, cpu);
        pcpu_rt = *ppcpu_rt;
        if (pcpu_rt)
        {
            rt6_rcu_free(pcpu_rt);
            *ppcpu_rt = NULL;
        }
    }
    free_percpu(non_pcpu_rt->rt6i_pcpu);
    non_pcpu_rt->rt6i_pcpu = NULL;
}