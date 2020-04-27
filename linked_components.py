input_filename = 'input.txt'
output_filename = 'output.txt'
input_file = open(input_filename, 'r')
output_file = open(output_filename, 'w')

n = int(input_file.readline())
links = [0] * (n + 1)
visited = [False] * (n + 1)
components = []


def write_result():
    output_file.write("{}\n".format(len(components)))
    for comp in components:
        output_file.write(" ".join(map(str, sorted(comp))) + " 0\n")


def dfs(v):
    component = []
    s = [v]
    visited[v] = True
    component.append(v)
    while s:
        current = s.pop()
        for i in range(1, n + 1):
            w = links[current][i - 1]
            if w and not visited[i]:
                visited[i] = True
                s.append(i)
                component.append(i)
    print(component)
    components.append(component)


def main():
    for i in range(1, n + 1):
        current_node = list(map(int, input_file.readline().split()))
        links[i] = current_node
    print(links)
    for v in range(1, n + 1):
        if not visited[v]:
            dfs(v)
    write_result()
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
