public class java
{
public static void main (String[] args)
{		
System.out.println("prime numbers from 1 to 100 are:");
for(int i=2;i<=100;i++)
{
if(isprime(i))
{
System.out.println(i+"");
}
}
}
public static boolean isprime(int num)
{ 		  	  
if(num<2)
return false;	  
for(int i=2;i<=Math.sqrt(num);i++)
{
if(num%i==0)
return false;
}
return true;
}
}