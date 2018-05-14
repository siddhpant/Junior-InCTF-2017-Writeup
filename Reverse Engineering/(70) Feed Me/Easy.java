import java.util.Scanner; 
class Easy {
	int len; 
	String input;
	String flag = "25d9d1cfc2e9ca5dc8239371c5dfb778";
	String a, b, c, d;
	StringBuilder e = new StringBuilder();
        StringBuilder f = new StringBuilder();
	String flag_format = "inctfj{";

	void input() {
                Scanner s = new Scanner(System.in);
		System.out.println("Enter the Correct Input:"); 
		input = s.nextLine();
	}

        void jumble() {
		len = input.length();
		a = input.substring(0, len / 4);
                b = input.substring(len / 4, len / 2);
                c = input.substring(len / 2, (3 * len) / 4);
		d = input.substring((3 * len) / 4, len);
		e.append(b);
		b = e.reverse().toString();
		f.append(d);
		d = f.reverse().toString();
        }

	void concatenate() {
		if (a.equals(flag.substring(0, 8))) {
			System.out.println("Pass 1 Complete");
			if (b.equals(flag.substring(8, 16))) {
	                        System.out.println("Pass 2 Complete");
				if (c.equals(flag.substring(16, 24))) {
		                        System.out.println("Pass 3 Complete");
					if (d.equals(flag.substring(24, 32))) {
			                        System.out.println("Pass 4 Complete");
						System.out.println("That is the right input.");
						System.out.println("The flag is:");
                                                System.out.println(flag_format + a + b + c + d + "}");
					}
				}
			}
		}
		else
			System.out.println("Nope");
	}


	public static void main(String args[]) {
		Easy ques = new Easy();
		ques.input();
		ques.jumble();
		ques.concatenate();
	}
}
