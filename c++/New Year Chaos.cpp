void minimumBribes(vector<int> q) {
    int swapcount=0;
    for(int i=q.size()-1;i>0;i--){
        if(q[i]!=i+1){
            
            if(((i-1)>=0) && q[i-1]==(i+1)){
                swapcount+=1;
                //swap(q,i,i-1);
                q[i]=q[i]^q[i-1];
                q[i-1]=q[i]^q[i-1];
                q[i]=q[i]^q[i-1];
            }
            else if(((i-1)>=0)&&q[i-2]==(i+1)){
                swapcount+=2;
                //swap(q,i-1,i-2);
                q[i-1]=q[i-2]^q[i-1];
                q[i-2]=q[i-2]^q[i-1];
                q[i-1]=q[i-2]^q[i-1];
                //swap(q,i-1,i)
                q[i]=q[i]^q[i-1];
                q[i-1]=q[i]^q[i-1];
                q[i]=q[i]^q[i-1];
            }
            else{
                cout<<"Too chaotic"<<endl;
                return;
            }
        }
    }
    
    cout<<swapcount<<endl;

}