/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */

var canFinish = function(numCourses, prerequisites) {
    // create graph
    var graph = [];
    for(let i = 0; i < numCourses; i++){
        graph[i] = [];
    }
    var visited = [];
    for(let i = 0; i < numCourses; i++){
        visited[i] = 0;
    }
    //
    prerequisites.forEach(function(x){
        graph[x[0]].push(x[1]);
    });

    var dfs = function(graph, visited, i){
        if(visited[i] === -1){//if ith node is marked as being visited, then a cycle is found
            return false;
        }
        if(visited[i] === 1){//if it is done visted, then do not visit again
            return true;
        }
        visited[i] = -1;

        for(let j = 0; j < graph[i].length; j++){
            if(!dfs(graph,visited,graph[i][j])){
                return false;
            }
        }
        visited[i] = 1;
        return true;
    };

    for(let i = 0; i < numCourses; i++){
        if(!dfs(graph, visited, i)){
            return false;
        }
    }
    return true;
};

