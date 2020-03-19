#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<string>
#include<iomanip>
#include<sstream>
using namespace std;
int main(){
	cout<<"input:"<<endl;
	char s[100];
	cin>>s;
	
	char key[100]={0};
	int val[100]={0};
	int p=0;
	int i=0;
	int j=0;
	for(i=0;i<strlen(s);i++){
		for(j=0;j<strlen(key);j++){
			if(s[i]==key[j]){
				p=1;
				break;
			}
		}
		if(p==0){
			int k=0;
			k=strlen(key);
			key[k]=s[i];
			val[k]+=1;
		}
		if(p==1){
			val[j]+=1;
		}
		p=0;
	}
	cout<<"keys & values:"<<endl;
	for(i=0;i<strlen(key);i++){
		cout<<key[i]<<" ";
	}
	cout<<endl;
	for(i=0;i<strlen(key);i++){
		cout<<val[i]<<" ";
	}
	cout<<endl;
	
	long double percentage[100]={0.0};
	int sum=strlen(s);
	for(i=0;i<strlen(key);i++){
		percentage[i]=(1.0*val[i])/sum;
	}
	long double left[100]={0.0};
	long double right[100]={0.0};
/*	left[strlen(key)-1]=0.0;
	right[strlen(key)-1]=percentage[strlen(key)-1];
	for(i=strlen(key)-2;i>=0;i--){
		left[i]=right[i+1];
		right[i]=left[i]+percentage[i];
	}*/
	left[0]=0.0;
	right[0]=percentage[0];
	for(i=1;i<strlen(key);i++){
		left[i]=right[i-1];
		right[i]=left[i]+percentage[i];
	}
	for(i=0;i<strlen(key);i++){
		cout<<setprecision(65)<<percentage[i]<<" "<<setprecision(65)<<left[i]<<" "<<setprecision(65)<<right[i]<<endl;
	}
	
	cout<<"\n------- ENCODING -------"<<endl;
	long double lb=0.0;
	long double ub=1.0;
	long double range=1.0;
	int index=0;
	for(i=0;i<sum;i++){
		cout<<setprecision(65)<<lb<<" "<<setprecision(65)<<ub<<" "<<endl;
		for(j=0;j<strlen(key);j++){
			if(s[i]==key[j]){
				index=j;
				break;
			}
		}
		range=ub-lb;
		ub=right[index]*range*1.0+lb;
		lb=left[index]*range*1.0+lb;
	}
	cout<<setprecision(65)<<lb<<" "<<setprecision(65)<<ub<<" "<<endl;
	long double tag=0.0;
	tag=(lb+ub)/2.0;
	cout<<"\ntag:"<<setprecision(65)<<tag<<endl;
	
	cout<<"\n------- DECODING -------"<<endl;
	lb=0.0;
	ub=1.0;
	char ret[100]={0};
	long double temp=0;
	for(i=0;i<sum;i++){
		temp=((tag-lb)*1.0)/(ub-lb);
		for(j=0;j<strlen(key);j++){
			if(temp>=left[j]){
				if(temp<right[j]){
					ret[i]=key[j];
					lb=left[j];
					ub=right[j];
					tag=temp;
					break;
				}	
			}
		}
	}
	cout<<"The decoded Sequence is:"<<endl;
	cout<<ret<<endl;
} 
