from collections import defaultdict


def get_paths_from(current_path, connections, all_paths, visited_twice=False):
    # takes a minute or few on my machine
    current = current_path[-1]
    paths = connections[current]
    valid_paths = []
    for path in paths:
        local_visited = visited_twice
        if path == "start":
            continue
        if path.islower() and path in current_path:
            if local_visited:
                continue
            local_visited = True
        if path == "end":
            if path in all_paths:
                continue
            valid_paths.append(current_path + [path])
            all_paths.append(current_path + [path])
        else:
            other_paths = get_paths_from(current_path + [path], connections, all_paths, local_visited)
            valid_paths += other_paths

    return valid_paths


def main():
    with open("input.txt", "r") as f:
        connections_from = defaultdict(list)
        all_paths = []
        for line in f.readlines():
            s, e = line.strip().split("-")
            connections_from[s].append(e)
            connections_from[e].append(s)
        ans = get_paths_from(["start"], connections_from, all_paths)
        print(len(ans))


if __name__ == '__main__':
    main()


"""
p1

from collections import defaultdict


def get_paths_from(current_path, connections, all_paths, previous=None):
    current = current_path[-1]
    paths = connections[current]
    # if current_path == ['start', 'HN', 'dc']:
    #     print(paths)
    valid_paths = []
    for path in paths:
        # if path == previous:
        #     continue
        if path.islower() and path in current_path:
            continue
        # if current_path == ['start', 'HN', 'dc']:
        #     print(path)
        if path == "end":
            if path in all_paths:
                continue
            valid_paths.append(current_path + [path])
            all_paths.append(current_path + [path])
        else:
            other_paths = get_paths_from(current_path + [path], connections, all_paths, current)
            valid_paths += other_paths

    return valid_paths


def main():
    with open("input.txt", "r") as f:
        connections_from = defaultdict(list)
        all_paths = []
        for line in f.readlines():
            s, e = line.strip().split("-")
            connections_from[s].append(e)
            connections_from[e].append(s)
        ans = get_paths_from(["start"], connections_from, all_paths)
        # print("\n")
        # for a in ans:
        #     print(a)
        print(len(ans))

"""