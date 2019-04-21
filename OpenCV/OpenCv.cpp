// OpenCv.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include<opencv2/opencv.hpp>
#include<iostream>
using namespace std;
using namespace cv;
int main()
{

	Mat img = imread("C:/Users/Akhil/Desktop/opencv/OpenCv/lena.jpg");
	if (img.empty())
		cout << "failed to open img.jpg lolz " <<endl;
	else
		cout << "img.jpg loaded OK" << endl;
	namedWindow("image", WINDOW_NORMAL);
	imshow("image", img);
	waitKey(0);
	return 0;

}

