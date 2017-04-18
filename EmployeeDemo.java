import java.time.LocalDate;
import java.util.Random;
class Employee {
	private String name = "";
	public double salary;
	private int id;
	private LocalDate hireDay;
	private static int indexId;
	static{
		Random generator = new Random();
		indexId = generator.nextInt(10000);
	}
	{
		id = indexId;
		indexId++;
	}
	public Employee(String n,double s){
		this.name = n;
		this.salary = s;
		this.hireDay = LocalDate.now();
	}
	public Employee(String n){
		this(n,0);
	}
	public Employee(){
		
	}
	public int getId(){
		return id;
	}
	public double getSalary(){
			return this.salary;
	}
	public String getName(){
			return this.name;
	}
	public LocalDate getHireDay(){
		return this.hireDay;
	}
}
