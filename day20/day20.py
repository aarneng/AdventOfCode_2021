from copy import deepcopy


def enhance(image, mapping, n=2):
    for enhancement in range(n):
        if enhancement % 2 == 0:
            image = [list(".......") + line + list(".......") for line in image]
            to_add = [["." for __ in range(len(image[0]))] for _ in range(7)]
            image = to_add + image + to_add
        image = [[i for i in sublist] for sublist in image]  # resulting image gets additional lit pixels otherwise
        output = deepcopy(image)

        c = 0
        for i in range(len(image)):
            for j in range(len(image[0])):
                c += 1
                if i == 0:
                    continue
                if j == 0:
                    continue
                try:
                    all_pixels = [image[i + dx][j + dy] for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
                    pixels_as_num = 0
                    for pixel in all_pixels:
                        pixels_as_num <<= 1
                        pixels_as_num += pixel == "#"
                    output[i][j] = mapping[pixels_as_num]
                except IndexError:
                    pass

        output = [i[1:-1] for i in output[1:-1]]

        image = deepcopy(output)

    return image


def count_lit_pixels(img):
    return sum([i.count("#") for i in img])


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        mapping = lines[0]
        lines = [list(i.strip()) for i in lines[2:]]
        enhanced = enhance(lines, mapping)
        print("part 1")
        print(count_lit_pixels(enhanced))

        enhanced = enhance(lines, mapping, 50)
        print("part 2")
        print(count_lit_pixels(enhanced))


if __name__ == '__main__':
    main()

