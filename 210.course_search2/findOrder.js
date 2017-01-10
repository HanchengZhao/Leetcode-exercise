/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
    var graph = [];
    for(let i = 0; i < numCourses; i++){
        graph[i] = [];
    }
    prerequisites.forEach(function(x){
        graph[x[1]].push(x[0]);
    });
    //initialized graph and visited arrays
    var visited = [];
    for(let i = 0; i < numCourses; i++){
        visited[i] = 0;
    }

    var dfs = function(i,graph,visited,record){
        //if has been visited
        if(visited[i] == 1){
            return true;
        }
        //if is being visited
        if(visited[i] == -1){
            return false;
        }
        visited[i] = -1;

        for(let j = 0; j < graph[i].length; j++){
            if(!dfs(graph[i][j],graph,visited,record)){
                return false;
            }
        }
        record.push(i);
        visited[i] = 1;
        return true;

    };
    var record = [];
    for(let i = 0; i < numCourses; i++){
        if(!dfs(i,graph,visited,record)){
            return [];
        }
    }
    return record.reverse();

};