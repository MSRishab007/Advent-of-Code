#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main()
{
    ifstream file("input.txt");
    string line;
    int answer=0;
    int answer2=0;
    int position=50;
    char direction;
    int value;
    if (file.is_open()) {
        while (getline(file, line)) {
            direction=line[0];
            value=stoi(line.substr(1));
            answer2+=value/100;
            value=value%100;
            if (direction=='L')
            {
                if (position!=0 && (position-value)<=0)
                {
                    answer2+=1;
                }
                position-=value;
            }
            else 
            {
                position+=value;
                if (position>=100)
                {
                    answer2+=1;
                }
            }
            position%=100;
            position %= 100;
            if (position < 0) 
            {
                position += 100;
            }
            if (position==0)
            {
                answer+=1;
                // answer2+=1;
            }
        }
        file.close();
    }
    else {
        cerr << "Unable to open file!" << endl;
    }
    cout << "First Answer: " << answer << endl;
    cout << "Second Answer: " << answer2 << endl;

    return 0;
}