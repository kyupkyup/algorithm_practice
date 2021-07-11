class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class NodeMgmt {
  constructor(head) {
    this.head = head;
  }

  insert(value) {
    this.currentNode = this.head;

    while (true) {
      if (value < this.currentNode.value) {
        if (this.currentNode.left !== null) {
          this.currentNode = this.currentNode.left;
        } else {
          this.currentNode.left = new Node(value);
          break;
        }
      } else if (this.currentNode.right !== null) {
        this.currentNode = this.currentNode.right;
      } else {
        this.currentNode.right = new Node(value);
        break;
      }
    }
  }

  search(value) {
    this.currentNode = this.head;
    while (this.currentNode) {
      if (this.currentNode.value === value) {
        return true;
      }
      if (value < this.currentNode.value) {
        this.currentNode = this.currentNode.left;
      } else {
        this.currentNode = this.currentNode.right;
      }
    }
    return false;
  }

  delete(value) {
    let searched = false;
    this.currentNode = this.head;
    this.parent = this.head;
    while (this.currentNode) {
      if (this.currentNode.value === value) {
        searched = true;
        break;
      } else if (value < this.currentNode.value) {
        this.currentNode = this.currentNode.left;
      } else {
        this.currentNode = this.currentNode.right;
      }
    }
    if (!searched) return false;

    if (this.currentNode.left === null && this.currentNode.right === null) {
      if (value < this.parent.value) {
        this.parent.left = null;
      } else {
        this.parent.right = null;
      }
      delete this.currentNode;
    }
    if (this.currentNode.left !== null && this.currentNode.right === null) {
      if (value < this.parent.value) {
        this.parent.left = this.current.left;
      } else {
        this.parent.right = this.currentNode.left;
      }
    } else if (this.currentNode.left === null && this.currentNode.right !== null) {
      if (value < this.parent.value) {
        this.parent.left = this.currentNode.right;
      } else {
        this.parent.right = this.currentNode.right;
      }
    }
    if (this.currentNode.left != null && this.currentNode.right !== null) {
      if (value < this.parent.left) {
        this.changeNode = this.currentNode.right;
        this.changeNodeParent = this.parent;
        while (this.changeNode.left !== null) {
          this.changeNodeParent = this.changeNode;
          this.changeNode = this.changeNode.left;
        }
        if (this.changeNode.right != null) {
          this.changeNodeParent.left = this.changeNode.right;
        } else {
          this.changeNodeParent.left = null;
        }
        this.parent.right = this.changeNode;
        this.changeNode.left = this.currentNode.left;
        this.changeNode.right = this.currentNode.right;
      }
    }
    return true;
  }
}

const bstNums = new Set();
while (bstNums.size !== 100) {
  bstNums.add(Math.floor(Math.random() * 100));
}
const head = new Node(50);
const binaryTree = new NodeMgmt(head);
for (const num of bstNums) {
  binaryTree.insert(num);
}
for (const num of bstNums) {
  if (!binaryTree.search(num)) console.log('fail' + num);
  console.log(binaryTree.search(num));
}
console.dir(binaryTree);
