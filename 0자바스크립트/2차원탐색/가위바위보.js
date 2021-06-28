const solution = (N, arr1, arr2) =>{
    for(let i = 0; i< arr1.length; i++){
        if(arr1[i] === 1){
            if(arr2[i] === 2){
                console.log('B');
            }
            else if(arr2[i] === 3){
                console.log('A');
            }
            else{
                console.log('D')
            }
        }
        else if(arr1[i] === 2){
            if(arr2[i] === 1){
                console.log('A');
            }
            else if(arr2[i] === 3){
                console.log('B');
            }
            else{
                console.log('D')
            }
        }
        else if(arr1[i] === 3){
            if(arr2[i] === 1){
                console.log('B');
            }
            else if(arr2[i] === 2){
                console.log('A');
            }
            else{
                console.log('D')
            }
        }
    }
}

solution(5, [2,3,3,1,3], [1,1,2,2,3])