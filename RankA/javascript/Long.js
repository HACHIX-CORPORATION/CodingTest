(function main() {
    //var array=[1 ,0 ,1 ,1 ,1 ,1 ,1 ,1 ,0];
     //var array=[1 ,1 ,1 ,1 ,1 ,0 ,0 ,1 ,1 ,1 ,1 ,1 ,0 ,0];

    var n=array.length;
    var maxLength=0;
    var checkTrue=function(array1){
        var dem =0;
        for(var i=0;i<array1.length;i++){
            if(array1[i]==0){
                dem++;
            }
        }
        if(dem<2) return false;
        return true;
    }
    var checkTrueAllChil=function(array2){
        var arrTemp1=[];
        for(var j=i;j<n-1;j++){
            var dem=0;
            if(j-i>=7){
                for(var k=i;k<j+1;k++){
                    arrTemp1[dem++]=array[k];
                }
            if(checkTrue(arrTemp1)==false) return false;
            return true;
    }}
}
    for(var i=0;i<n-1;i++){
        var arrTemp=[];
        for(var j=i;j<n-1;j++){
            var dem=0;
            if(j-i>=7){
                for(var k=i;k<j+1;k++){
                    arrTemp[dem++]=array[k];
                }
                // var dem=0;
                // for(var l=0;l<arrTemp.length;l++){
                //     if(arrTemp[l]==0){
                //         dem++;
                //     }
                // }
                if(checkTrue(arrTemp)==true&& arrTemp.length>maxLength && checkTrueAllChil(arrTemp)==true){
                    maxLength = arrTemp.length;
                   console.log(arrTemp);

                }
            }

        }
    }
     if(maxLength==0) {console.log(maxLength);}
    else {console.log(maxLength+1);}

}());