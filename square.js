function square_sums_row(n) {
    if (n === 1) return [1];
    if (n === 2) return false; 
    let squares = new Set();
    for (let i = 2; i * i <= 2 * n - 1; i++) {
        squares.add(i * i);
    }
    let adj = new Array(n + 1).fill(0).map(() => []);
    for (let i = 1; i <= n; i++) {
        for (let j = i + 1; j <= n; j++) {
            if (squares.has(i + j)) {
                adj[i].push(j);
                adj[j].push(i);
            }
        }
    }

    for (let i = 1; i <= n; i++) {
        adj[i].sort((a, b) => adj[a].length - adj[b].length);
    }

    let path = new Array(n);
    let visited = new Array(n + 1).fill(false);

    function backtrack(count, currentNum) {
        if (count === n) {
            return true; 
        }

        for (let nextNum of adj[currentNum]) {
            if (!visited[nextNum]) {
                visited[nextNum] = true;
                path[count] = nextNum;
                if (backtrack(count + 1, nextNum)) {
                    return true;
                }
                visited[nextNum] = false; 
            }
        }
        return false;
    }
    let startNumbers = Array.from({ length: n }, (_, i) => i + 1)
                                .sort((a, b) => adj[a].length - adj[b].length);

    for (let startNum of startNumbers) {
        visited.fill(false); 
        visited[startNum] = true;
        path[0] = startNum;
        if (backtrack(1, startNum)) {
            return path;
        }
    }
    return false; 
}

