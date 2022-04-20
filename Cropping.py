import cv2

import GetResults


class Cropping:
    __cropping = False
    __x_start, __y_start, __x_end, __y_end = 0, 0, 0, 0
    __counter = 0
    Cropping_Result = [[]]
    __Flag = True

    def __init__(self, ImagePath):
        self.image = cv2.imread(ImagePath)
        self.oriImage = self.image.copy()
        self.p1 = GetResults.GetResults()

    def mouse_crop(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.__x_start, self.__y_start, self.__x_end, self.__y_end = x, y, x, y
            self.__cropping = True


        elif event == cv2.EVENT_MOUSEMOVE:
            if self.__cropping:
                self.__x_end, self.__y_end = x, y


        elif event == cv2.EVENT_LBUTTONUP:

            self.__x_end, self.__y_end = x, y
            self.__cropping = False

            self.refPoint = [(self.__x_start, self.__y_start), (self.__x_end, self.__y_end)]

            if len(self.refPoint) == 2:
                #aprint('HI')
                global counter
                roi = self.oriImage[self.refPoint[0][1]:self.refPoint[1][1], self.refPoint[0][0]:self.refPoint[1][0]]
                self.p1.insert(roi)
                list_result = self.p1.get_result()
                self.Cropping_Result[len(self.Cropping_Result) - 1] += list_result
                print(list_result)
                self.Cropping_Result.append([])
                if cv2.waitKey(150) == ord('a'):
                    print('quit')
                    self.__Flag = False
                else:
                    self.__Flag = True
                self.__counter += 1
                cv2.imshow("Cropped", roi)

    def __start(self):
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.mouse_crop)

    def run(self):
        self.__start()
        while self.__Flag:
            i = self.image.copy()
            if not self.__cropping:
                cv2.imshow("image", self.image)
            elif self.__cropping:
                cv2.rectangle(i, (self.__x_start, self.__y_start), (self.__x_end, self.__y_end), (255, 0, 0), 2)
                cv2.imshow("image", i)

            cv2.waitKey(1)
        # self.__Cropping_Result.pop()
        cv2.destroyAllWindows()
        return self.Cropping_Result
