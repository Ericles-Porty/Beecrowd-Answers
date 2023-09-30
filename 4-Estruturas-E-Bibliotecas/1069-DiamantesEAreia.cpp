#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

string limpaAreia(string mina)
{
    string minalimpa;
    for (int i = 0; i < mina.length(); i++)
        if (mina[i] != '.')
            minalimpa += mina[i];
    return minalimpa;
}

int main()
{
    int contador = 0;
    string mina;

    int nRuns;
    cin >> nRuns;
    for (int i = 0; i < nRuns; i++)
    {
        cin >> mina;

        mina = limpaAreia(mina);

        int tamanhoMina = mina.length();

        int posLess = -1, posGreater = -1;

        for (int j = 0; j < tamanhoMina; j++)
        {
            if (mina[j] == '<')
            {
                posLess = j;
            }

            if (mina[j] == '>')
            {
                posGreater = j;
            }

            if (posLess != -1 && posLess < posGreater)
            {
                contador++;

                mina.erase(posGreater, 1);
                mina.erase(posLess, 1);
                tamanhoMina -= 2;

                j = -1;
                posLess = -1;
                posGreater = -1;
            }
        }
        cout << contador << endl;
        contador = 0;
    }
    return 0;
}