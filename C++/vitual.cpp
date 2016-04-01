/*************************************************************************
  > File Name: vitual.cpp
  > Author: Ulric
  > Mail: 675962721@qq.com 
  > Created Time: Wed 09 Mar 2016 10:43:01 AM CST
 ************************************************************************/
#include <iostream>
#include <string>

using namespace std;

enum COLOR{ RED, GREEN, COLOR_SIZE };
string color_str_[COLOR_SIZE] = {"RED", "GREEN"};

class Shape
{
	public:
		virtual void draw(COLOR color=RED) const
		{   
			cout << "Shape:" << color_str_[color] << endl;
		}   
};

class Circle : public Shape
{
	public:
		virtual void draw(COLOR color=GREEN) const
		{   
			cout << "color:" << color << endl;
			cout << "Circle:" << color_str_[color] << endl;
		}   
};

int main()
{
	Shape* ps = new Circle();
	ps -> draw();
	delete ps;
	return 0;
}
