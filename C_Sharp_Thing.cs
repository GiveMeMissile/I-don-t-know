using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        Console.WriteLine("What is 12*10?: ");
        int answer = 0;
        while (true)
        {
            try
            {
                answer = Convert.ToInt32(Console.ReadLine());
                break;
            }
            catch (Exception e)
            {
                Console.WriteLine("Try again fellow. Make sure to input a number Idiot.");
            }
        }
        if (answer == 120)
        {
            Console.WriteLine("You are correct!");
        }
        else
        {
            Console.WriteLine("You are Incorrect IDIOT!!!");
        }
            
        
    }
