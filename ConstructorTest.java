
public class ConstructorTest {
	public static void main(String[] args) {
		Manager boss = new Manager("����",2500.0);
		Employee[] staff = new Employee[3];
		staff[0] = new Employee("����һ",2000.0);
		staff[1] = new Employee("���격",3000.0);
		staff[2] = boss;
		boss.setBonus(1000.0);
		for(Employee e:staff){
			System.out.println("name="+e.getName()+",id="+e.getId()+",salary="+e.getSalary());
		}
	}
}
