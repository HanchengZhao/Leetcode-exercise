/*
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 6 and 8 have a common ancestor of 4.

         14  13
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

parentChildPairs1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

Sample input and output:

hasCommonAncestor(parentChildPairs1, 3, 8) => false
hasCommonAncestor(parentChildPairs1, 5, 8) => true
hasCommonAncestor(parentChildPairs1, 6, 8) => true
hasCommonAncestor(parentChildPairs1, 6, 9) => true
hasCommonAncestor(parentChildPairs1, 1, 3) => false
hasCommonAncestor(parentChildPairs1, 7, 11) => true
hasCommonAncestor(parentChildPairs1, 6, 5) => true
hasCommonAncestor(parentChildPairs1, 5, 6) => true

Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

        11
       /  \
      10   12
     /  \
1   2    5
 \ /    / \
  3    6   7
   \        \
    4        8

parentChildPairs2 = [
    (11, 10), (11, 12), (10, 2), (10, 5), (1, 3),
    (2, 3), (3, 4), (5, 6), (5, 7), (7, 8),
]

hasCommonAncestor(parentChildPairs2, 4, 12) => true
hasCommonAncestor(parentChildPairs2, 1, 6) => false
hasCommonAncestor(parentChildPairs2, 1, 12) => false
*/

let parentChildPairs1 = [
  [1, 3],
  [2, 3],
  [3, 6],
  [5, 6],
  [5, 7],
  [4, 5],
  [4, 8],
  [4, 9],
  [9, 11],
  [14, 4],
  [13, 12],
  [12, 9],
];

let parentChildPairs2 = [
  [11, 10],
  [11, 12],
  [10, 2],
  [10, 5],
  [1, 3],
  [2, 3],
  [3, 4],
  [5, 6],
  [5, 7],
  [7, 8],
];

function getChildWithZeroOrOneParents(pairs) {
  let parents = {};
  let elements = new Set();
  for (let i = 0; i < pairs.length; i++) {
    let [parent, child] = pairs[i];
    if (child in parents) {
      parents[child].push(parent);
    } else {
      parents[child] = [parent];
    }
    elements.add(parent);
    elements.add(child);
  }
  let zeroParent = [];
  let oneParent = [];
  elements.forEach(ele => {
    let eleString = ele.toString();
    // no parent
    if (!parents.hasOwnProperty(eleString)) {
      zeroParent.push(ele);
    } else {
      if (parents[eleString].length === 1) {
        oneParent.push(ele);
      }
    }
  });
  return [zeroParent, oneParent];
}
// console.log(getChildWithZeroOrOneParents(parentChildPairs))

function getAllParents(pairs, node) {
  let parents = [];
  pairs.forEach(p => {
    if (p[1] === node) {
      parents.push(p[0]);
    }
  });
  let newParents = [];
  parents.forEach(p => {
    newParents = newParents.concat(getAllParents(pairs, p));
  });
  console.log(parents.concat(newParents));
  return parents.concat(newParents);
}

function hasCommonAncestor(pairs, node1, node2) {
  let parents1 = getAllParents(pairs, node1);
  let parents2 = getAllParents(pairs, node2);
  for (let i = 0; i < parents1.length; i++) {
    for (let j = 0; j < parents2.length; j++) {
      if (parents1[i] == parents2[j]) {
        return true;
      }
    }
  }
  return false;
}
console.log(getAllParents(parentChildPairs1, 6));
console.log(hasCommonAncestor(parentChildPairs1, 1, 2));
