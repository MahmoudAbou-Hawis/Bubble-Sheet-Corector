import cv2


class GetResults:
    __Number_list = [[]]
    __List = []
    __Final_Result = []
    __answer_list = []
    __All_answers = [[]]
    __X_list = [1, -1, 1, -1, 0, 1, -1, 0]
    __Y_list = [1, -1, -1, 1, 1, 0, 0, -1]
    __visited = set()

    def __init__(self):
        self.__black_and_white_image = None
        self.__grayImage = None

    def insert(self, original):
        self.__rest()
        self.__grayImage = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        (self.__thresh, self.__blackAndWhiteImage) = cv2.threshold(self.__grayImage, 209, 255, cv2.THRESH_BINARY)
        self.__black_and_white_image = self.__blackAndWhiteImage

    def __rest(self):
        self.__visited.clear()
        self.__List.clear()
        self.__Final_Result.clear()
        self.__All_answers.clear()
        self.__answer_list.clear()
        self.__Number_list.clear()
        self.__Number_list.append([])
        self.__All_answers.append([])

    def __questions_in_paper(self):
        for i in range(self.__black_and_white_image.shape[0]):
            black = 0
            white = 0
            for e in range(self.__black_and_white_image.shape[1]):
                if self.__black_and_white_image[i][e] == 0:
                    black += 1
                    self.__List.append((i, e))
                    break
                else:
                    white += 1
            if black == 0:
                if len(self.__List) > 0:
                    self.__Number_list[len(self.__Number_list) - 1] += self.__List
                    self.__Number_list.append([])
                    self.__List.clear()
        self.__Number_list[len(self.__Number_list) - 1] += self.__List

    def __valid(self, x, y):
        return 0 <= x < self.__black_and_white_image.shape[0] and 0 <= y < self.__blackAndWhiteImage.shape[1]

    def __marked_answer(self, x, y):
        self.__visited.add((x, y))
        ret = 0
        for i in range(8):
            if self.__valid(x + self.__X_list[i], self.__Y_list[i] + y):
                if (x + self.__X_list[i], self.__Y_list[i] + y) not in self.__visited and \
                        self.__blackAndWhiteImage[x + self.__X_list[i]][self.__Y_list[i] + y] == 0:
                    ret += self.__marked_answer(x + self.__X_list[i], self.__Y_list[i] + y)
        return 1 + ret

    def __find_all_answers(self):
        for List in self.__Number_list:
            if len(List) > 0:
                midN = len(List) // 2
                x, y = List[midN]
                for i in range(y, self.__blackAndWhiteImage.shape[1]):
                    if self.__blackAndWhiteImage[x][i] == 0 and (x, i) not in self.__visited:
                        self.__answer_list += [self.__marked_answer(x, i)]
                self.__All_answers[len(self.__All_answers) - 1] += self.__answer_list
                self.__answer_list.clear()
                self.__All_answers.append([])

    def __result(self):
        for Answer in self.__All_answers:
            if len(Answer) > 0:
                mx = 0
                for i in range(len(Answer)):
                    if Answer[i] > Answer[mx]:
                        mx = i
                if len(Answer) > 4:
                    self.__Final_Result.append((mx // 2) + 1)
                else:
                    self.__Final_Result.append(mx + 1)

    def get_result(self):
        self.__questions_in_paper()
        self.__find_all_answers()
        self.__result()
        return self.__Final_Result
