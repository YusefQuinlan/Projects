package CSVmake;

public class Person {
	private int age;
	private String fName;
	private String lName;
	private String id;
	
	Person(int anAge, String anFName, String aLName
			, String anId){
		this.age = anAge;
		this.fName = anFName;
		this.lName = aLName;
		this.id = anId;
		
	}
	void setfname(String anFName) {
		this.fName = anFName;
	}
	void setlname(String anLName) {
		this.lName = anLName;
	}
	void setage(int anAge) {
		this.age= anAge;
	}
	void setid(String anId) {
		this.id = anId;
	}
	String getfname() {
		return this.fName;
	}
	String getlname() {
		 return this.lName;
	}
	int getage() {
		return this.age;
	}
	String getid() {
		return this.id;
	}
}

