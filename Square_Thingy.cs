// I made this becase I don't wanna calculate the square on my homework.
// So I just made this program to do this for me (:

using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        Console.WriteLine("What is your number?");
        int number = Convert.ToInt32(Console.ReadLine());
        int square = CalculateSquare(number);
        if (square == -1)
        {
            Console.WriteLine("There is no squarable value that is contained in your number.");
        }
        else
        {
            Console.WriteLine("Your square value is "+square+".");
        }
    }
    
    public static int CalculateSquare(int num)
    {
        int[] squares= {225, 196, 169, 144, 121, 100, 81, 64, 49, 36, 25, 16, 9, 4};
        for (int i = 0; i < squares.Length; i++)
        {
            if (num % squares[i] == 0)
            {
                int square = squares[i];
                return square;
            }
        }
        return -1;
    }
}
