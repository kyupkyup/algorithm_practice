class Heap {
  constructor() {
    this.heapArray = [];
  }

  moveUp(insertedIdx) {
    if (insertedIdx <= 1) {
      return false;
    }

    const parentIdx = Math.floor(insertedIdx / 2);
    if (this.heapArray[insertedIdx] > this.heapArray[parentIdx]) {
      return true;
    }
    return false;
  }

  moveDown(poppedIdx) {
    const leftChildPoppedIdx = poppedIdx * 2;
    const rightChildPoppedIdx = poppedIdx * 2 + 1;

    if (leftChildPoppedIdx >= this.heapArray.length) {
      return false;
    }
    if (rightChildPoppedIdx >= this.heapArray.length) {
      if (this.heapArray[poppedIdx] < this.heapArray[leftChildPoppedIdx]) {
        return true;
      }
      return false;
    }

    if (this.heapArray[leftChildPoppedIdx] > this.heapArray[rightChildPoppedIdx]) {
      if (this.heapArray[poppedIdx] < this.heapArray[leftChildPoppedIdx]) {
        return true;
      }
      return false;
    }

    if (this.heapArray[poppedIdx] < this.heapArray[rightChildPoppedIdx]) {
      return true;
    }
    return false;
  }

  insert(value) {
    if (this.heapArray.length === 0) {
      this.heapArray.push(null);
      this.heapArray.push(value);
      return true;
    }
    this.heapArray.push(value);
    let insertedIdx = this.heapArray.length - 1;

    while (this.moveUp(insertedIdx)) {
      const parentIdx = Math.floor(insertedIdx / 2);
      const temp = this.heapArray[parentIdx];
      this.heapArray[parentIdx] = this.heapArray[insertedIdx];
      this.heapArray[insertedIdx] = temp;
      insertedIdx = parentIdx;
    }
    return true;
  }

  pop() {
    if (this.heapArray.length <= 1) {
      return null;
    }
    const returnedData = this.heapArray[1];
    this.heapArray[1] = this.heapArray[this.heapArray.length - 1];
    let poppedIdx = 1;

    while (this.moveDown(poppedIdx)) {
      const leftChildPoppedIdx = poppedIdx * 2;
      const rightChildPoppedIdx = poppedIdx * 2 + 1;

      if (rightChildPoppedIdx >= this.heapArray.length) {
        if (this.heapArray[poppedIdx] < this.heapArray[leftChildPoppedIdx]) {
          const temp = this.heapArray[poppedIdx];
          this.heapArray[poppedIdx] = this.heapArray[leftChildPoppedIdx];
          this.heapArray[leftChildPoppedIdx] = temp;
        }
        poppedIdx = leftChildPoppedIdx;
      } else if (this.heapArray[leftChildPoppedIdx] > this.heapArray[rightChildPoppedIdx]) {
        if (this.heapArray[poppedIdx] < this.heapArray[leftChildPoppedIdx]) {
          const temp = this.heapArray[poppedIdx];
          this.heapArray[poppedIdx] = this.heapArray[leftChildPoppedIdx];
          this.heapArray[leftChildPoppedIdx] = temp;
          poppedIdx = leftChildPoppedIdx;
        }
      } else if (this.heapArray[poppedIdx] < this.heapArray[rightChildPoppedIdx]) {
        const temp = this.heapArray[poppedIdx];
        this.heapArray[poppedIdx] = this.heapArray[rightChildPoppedIdx];
        this.heapArray[rightChildPoppedIdx] = temp;
        poppedIdx = rightChildPoppedIdx;
      }
    }
    return returnedData;
  }
}

const heap = new Heap();
heap.insert(3);
heap.insert(2);
heap.insert(4);
heap.insert(1);
heap.insert(6);
console.log(heap.pop());
console.log(heap.pop());
console.log(heap.pop());
console.log(heap.pop());
console.log(heap.pop());
