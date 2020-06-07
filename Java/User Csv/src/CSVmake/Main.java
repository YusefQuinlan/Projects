package CSVmake;
import java.io.*;
import java.util.Scanner;
public class Main {
/*
 This program essentially checks if a certain csv file exists, if it doesnt then it
 creates the csv file and adds basic titles for 4 columns. Regardless of whether it
 exists or not, it will then ask a user if they want to add a person to the csv file,
 if yes then users will be asked for various details of the person in a specific order.
 If there are any errors when asking for a specific detail a user will be asked for the detail
 again and informed that an error has occured. At the end of this proccess, the person and
 their details will be added to the csv file. If the user wishes to add another person at
 the end of the process they can, and the proccess will start again. The process only terminates
 when the user no longer wants to add people to the csv file (barring termination due to bugs
 and errors).
 
 */	

/*
 Just a few things I should mention, this is my first program ever outside of 
 my university course so it is a little rough. There are likely flaws in it and
 even I can see room for improvement. It is too complex and there are probably ways
 to put items into csv files based on user input, that are simpler that what I have done.
 I mainly wanted to make a successful program, also my first time dealing with files in
 Java, I imagine I could do better. The age string should only accept digits but it doesn't
 , this is simply because the point of the program is only to enter items into a csv rather
 than demonstrate string manipulation. The Exception handling is poor, but I tried to do
 at least the bare minimum. Person.Java isn't necessary, I just made it to practice basic
 Classes in Java again in case I needed a class for this implementation. All that being
 said I am open to critisicm and happy to hear how I could improve my work, so any suggestions
 would be appreciated.
 
 */
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		csvCheck();

	}
	
	public static void csvCheck() throws IOException 
	{
	File f = new File("Persons.csv");
	if(f.createNewFile()) {
		Scanner aScanner = new Scanner(System.in);
		System.out.println("Want to enter a person, Y/N?");
		String input = aScanner.nextLine();	
		FileWriter writeTo = new FileWriter("Persons.csv", true);
		writeTo.append("id,");
		writeTo.append("age,");
		writeTo.append("firstname,");
		writeTo.append("lastname");
		writeTo.write(System.lineSeparator());
		writeTo.close();
		if(input.toUpperCase().equals("Y")) {
			firstName();
		}
		else if(input.toUpperCase().equals("N")) {
			System.out.println("No people will be added to the database");
			aScanner.close();

			System.exit(0);
		}
		else {
			System.out.println("Make sure to respond with y or n, y for yes, n for no");
			csvCheck();
		}	
		
	}
	else {
		Scanner aScanner = new Scanner(System.in);
		System.out.println("Want to enter a person, Y/N?");
		String input = aScanner.nextLine();
		if(input.toUpperCase().equals("Y")) {
			firstName();
		}
		else if(input.toUpperCase().equals("N")) {
			System.out.println("No people will be added to the database");
			aScanner.close();
			System.exit(0);
		}
		else {
			System.out.println("Make sure to respond with y or n, y for yes, n for no");
			csvCheck();
		}
		
	}
    }
	
	public static void firstName() {
		Scanner aScanner = new Scanner(System.in);
		System.out.println("What is the first name of the person?");
		String input = aScanner.nextLine();		
		try {
			secondName(input);
		}
		catch (Exception e){
			System.out.println("An error has occured with the name input, we will ask again");
			firstName();			
		}
	}
		public static void secondName(String name) {
			Scanner aScanner = new Scanner(System.in);
			System.out.println("What is the second name of the person?");
			String input = aScanner.nextLine();
			
			try {
				age(input,name);
			}
			catch (Exception e){
				System.out.println("An error has occured with the name input, we will ask again");
				secondName(name);			
			}
	}
		public static void age(String secName, String firstName) {
			Scanner aScanner = new Scanner(System.in);
			System.out.println("What is the age of the person?");
			String input = aScanner.nextLine();
			try {
				id(input,secName,firstName);
			}
			catch (Exception e){
				System.out.println("An error has occured with the age input, we will ask again");
				age(secName,firstName);			
			}
	}
		public static void id(String age,String secName, String firstName) {
			Scanner aScanner = new Scanner(System.in);
			System.out.println("What is the id of the person?");
			String input = aScanner.nextLine();
			
			try {
				System.out.println("Person with id: " + input + " + age : " + age + 
						" + firstname : " + firstName + " + Secondname: " 
						+ secName + "is to be added to csv file.");
				writeToCsv(input, age, firstName, secName);
			}
			catch (Exception e){
				System.out.println("An error has occured with the id input, we will ask again");
				id(age,secName,firstName);			
			}
	}
		public static void writeToCsv(String id, String age, String first, String last) {
			try {
				FileWriter writeTo2 = new FileWriter("Persons.csv", true);
				writeTo2.append(id + ",");
				writeTo2.append(age + ",");
				writeTo2.append(first + ",");
				writeTo2.append(last);
				writeTo2.write(System.lineSeparator());
				writeTo2.close();
				Scanner aScanner = new Scanner(System.in);
				System.out.println("Want to add more people? y/n?");
				String input = aScanner.nextLine();
				if(input.toUpperCase().equals("Y")) {
					csvCheck();
				}
				else if(input.toUpperCase().equals("N")) {
					System.out.println("No more people will be added to the database");
					aScanner.close();
					System.exit(0);
				}
				else {
					System.out.println("Make sure to respond with y or n, y for yes, n for no");
					writeToCsv(id,age,first,last);
				}
				
			}
			catch (Exception e){
				System.out.println("Some weird error has occured, we'll try again");
				writeToCsv(id,age,first,last);
			}
		}
}