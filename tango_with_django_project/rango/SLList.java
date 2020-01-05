public class SLList{
	private class IntNode{
		public int item;
		public IntNode next;
		public IntNode(int item, IntNode next){
			this.item = item;
			this.next = next;
		}
	}

	private IntNode first;
	private int size;

	public void addFirst(int x){
		first = new IntNode(x, first);
		size += 1;
	}

	public void addLast(int x){
		if (first == null) {
			first = new IntNode(x, null)
		}else{
			IntNode pointer = first;
			while(pointer.next != null){
				pointer = pointer.next;
			}
			pointer.next = new IntNode(x, null);
		}
	}

	public SLList(int x){
		first = new IntNode(x, null);
		size = 1;
	}

	/**We need to first make sure */
	public  void insert(int item, int position){
		if (position >= size) {
			 addLast(item)
		}else{
			if (position == 0) {
				 addFirst(item)
			}else{
				int index = position;
				IntNode pointer = first;
				while(index - 1 != 0){
					pointer = pointer.next;
				}
				pointer.next =  new IntNode(item, pointer.next)
			}
		}
	}
}