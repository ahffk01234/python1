package day03;

public class Human extends Animal{
	boolean flag_coding;
	
	public void principle_voice() {
		flag_coding = true;
	}
	
	public static void main(String[] args) {
		Human hum = new Human();
		
		System.out.println(hum.flag_coding);
		System.out.println(hum.cnt_hair);
		
		hum.principle_voice();
		hum.tsshampoo();
		
		System.out.println(hum.flag_coding);
		System.out.println(hum.cnt_hair);
	}
	
}
