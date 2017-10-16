#include<iostream>
#include<stdio.h>
#include<cstdlib>
#include<ctime>
using namespace std;

class neuron
{
public:
	int n;
	int *x;
	int *w;
	int p;
	int learnRatio;
	neuron(int a,int *tab1,int *tab2,int b,int c)
	{
		n=a;
		x=tab1;
		w=tab2;
		p=b;
		learnRatio=c;
		x=new int[n];
		w=new int[n];
		for(int i=0;i<n;i++)
		{
			x[i]=(rand()%10+1)/10;
			w[i]=(rand()%10+1)/10;
		}
	}
	~neuron();
	int perceptron()
	{
		int out=0;
		for(int i=0;i<n;i++)
		{
			out+=w[i]*x[i];
		}
		return bpolar(out);
	}
	int bpolar(int x)
	{
		if(x<p)
		{
			return 0;
		}
		else
		{
			return 1;
		}
	}
	void learn(int d)
	{
		while(d!=perceptron())
		{
			for(int i=0;i<n;i++)
			{
				w[i]+=learnRatio*(d-perceptron())*x[i];
			}
		}
		for(int i=0;i<n;i++)
			{
				cout<<"waga:"<<w[i]<<endl;
		}
	}

			
};
int main()
{
	srand(time(NULL));
	int *tab,*tab1;
	neuron n(3,tab,tab1,1,0.5);
	cout<<"perceptron:"<<endl;
	cout<<n.perceptron()<<endl;
	n.learn(1);
	system("pause");
	return 0;
}
