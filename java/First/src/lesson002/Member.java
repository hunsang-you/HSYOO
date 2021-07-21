package lesson002;

public class Member {

	private int memberId; 		//회원 아이디
	private String memberName;	//회원 이름
	
	// 생성자 constructor
	public Member(int memberId, String memberName) {
		this.memberId = memberId;
		this.memberName = memberName; // this -> 위의 클래스로부터 생선된 객체의 
	}

	//getters, setters
	
	public int getMemberId() {
		return memberId;
	}

	public void setMemberId(int memberId) {
		this.memberId = memberId;
	}

	public String getMemberName() {
		return memberName;
	}

	public void setMemberName(String memberName) {
		this.memberName = memberName;
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return memberName + "회원님의 아이디는 " + memberId + "입니다.";
	}
	
	
	
	
	
}// end of main
