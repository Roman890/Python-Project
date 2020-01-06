
__kernel void part1(int size, __global float* a, __global float* b, __global float* c,  __global float* t)
{
    unsigned int in = get_global_id(0);
    float p1, p2;
    int len = size;

    printf("число = %d\n", len);
            for (int j=0; j<len; j++){
                p1=1; p2=1;
                for (int i=0; i<len; i++){
                        if (i==j){
                            p1=p1*1;p2=p2*1;
                        }
                        else {
                                p1=p1*(t[in]-a[i]);
                                p2=p2*(a[j]-a[i]);
                    }
                }
                c[in]=c[in]+b[j]*p1/p2;
        }

}