#include<stdio.h>

/* code by Donal
# april 13, 2022
# to calculate the first term, common difference, sum of first 20 terms of an AP given a4 and a6
*/


// Functions

/* This function takes inputs i,j,a_i,a_j and returns the  COMMON DIFFERENCE
         of the A.P whose a_i = i'th term and a_j = j'th term are given    */

int common_diff(int i,int j,int a_i,int a_j){
    
    int d = (a_j - a_i) / (j - i);
    return d;

}


/* This function takes inputs i,j,a_i,a_j and computes the  FIRST TERM
        of the A.P whose a_i = i'th term and a_j = j'th term are given   */


int first_term(int i,int j,int a_i,int a_j){
    
    int d = (a_j - a_i) / (j - i);
    int a_1 = a_i - (i - 1) * d;
    return a_1;

}

/*  This function takes inputs n,i,j,a_i,a_j and returns the " SUM OF n TERMS "
             of the A.P whose a_i = i'th term and a_j = j'th term are given   */


int Sum(int n,int i,int j,int a_i,int a_j){
    
   int  d = (a_j - a_i) / (j - i);
   int a_1 = a_i - (i - 1) * d;
   int  S_n = n / 2 * (2 * a_1 + (n - 1) * d);
   return S_n;

}


// Output to verify the correctness
int main(){

int n = 20;
int a_i = 8;
int a_j = 14;
int i = 4;
int j = 6;


int _d = common_diff(i, j, a_i, a_j);
int _a1 = first_term(i, j, a_i, a_j);
int _Sn = Sum(n, i, j, a_i, a_j);

printf("%d\n",_d);
printf("%d\n",_a1);
printf("%d\n",_Sn);


}