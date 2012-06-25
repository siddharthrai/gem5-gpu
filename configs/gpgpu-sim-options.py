
def addGPUOptions(parser):
    parser.add_option("--num_sc", default=-1, help="Number of shader cores in the gpu that GPGPU-sim is simulating", type="int")
    parser.add_option("--m5_cycles_per_gpu_cycles", default=1000000000000, help="Number of cycles m5 ticks per cycle gpgpu-sim ticks", type="int")
    parser.add_option("--gpu_ruby", default=True, help="hook gpu up to ruby instead of its internal memory")
    parser.add_option("--gpu_nonblocking", default=False, help="Make GPGPU kernels non-blocking")
    parser.add_option("--sc_l1_size", default="64kB", help="size of l1 cache hooked up to each sc")
    parser.add_option("--sc_l2_size", default="128kB", help="size of L2 cache divided by num L2 caches")
    parser.add_option("--sc_l1_assoc", default=4, help="associativity of l1 cache hooked up to each sc", type="int")
    parser.add_option("--sc_l2_assoc", default=16, help="associativity of L2 cache backing SC L1's", type="int")
    parser.add_option("--baseline", default=False, help="size of l1 cache hooked up to each sc")
    parser.add_option("--validation", default=False, help="size of l1 cache hooked up to each sc")
    parser.add_option("--fermi", default=False, help="size of l1 cache hooked up to each sc")
    parser.add_option("--gpu_only", default=False, help="Only time the GPU, use atomic CPU")
    parser.add_option("--shMemDelay", default=1, help="delay to access shared memory in gpgpu-sim ticks", type="int")

