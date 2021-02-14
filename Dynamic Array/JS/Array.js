/*
Array Data Structure in JavaScript
By: Suryakiran Santhosh
*/


`use strict`;


class ArrayDS {
    constructor(){
        this.array = [];
        this.length = 0;
    }
    
    // methods
    insert(val){
        this.array[this.length] = val;
        this.length++;
    }
    pop(){
        const item = this.array[this.array.length - 1];
        delete this.array[this.length - 1];
        this.length--;
        return item;
    }
    get(index) {
        return this.array[index];
    }
    indexOf(val){
        for(let i = 0; i <= this.length; i++){
            if (this.array[i] === val) {
                return i;
            }
        }
        return -1;  // -1 means the value was not in the array
    }
    removeAt(index){
        delete this.array[index];
        for(let i = index; i <= this.length; i++){
            this.array[i] = this.array[i+1];
        }
        delete this.array[this.length - 1];
        this.length--;
    }
}


(function main(){
    const arr = new ArrayDS();
    arr.insert(1);
    arr.insert(2);
    arr.insert(3);
    arr.insert(4);
    console.log(arr);
    console.log(arr.pop());
    console.log(arr);
    console.log(arr.indexOf(3));
    arr.removeAt(2);
    console.log(arr);
})()
