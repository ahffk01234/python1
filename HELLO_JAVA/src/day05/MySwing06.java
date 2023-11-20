package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JTextArea;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MySwing06 extends JFrame {

	private JPanel contentPane;
	JLabel lbl_first;
	JLabel lbl_last;
	JTextField tf_first;
	JTextField tf_last;
	JTextArea ta;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing06 frame = new MySwing06();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing06() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 397, 496);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl_first = new JLabel("첫별수");
		lbl_first.setBounds(90, 30, 57, 15);
		contentPane.add(lbl_first);
		
		lbl_last = new JLabel("끝별수");
		lbl_last.setBounds(90, 75, 57, 15);
		contentPane.add(lbl_last);
		
		tf_first = new JTextField();
		tf_first.setBounds(175, 27, 116, 21);
		contentPane.add(tf_first);
		tf_first.setColumns(10);
		
		tf_last = new JTextField();
		tf_last.setColumns(10);
		tf_last.setBounds(175, 72, 116, 21);
		contentPane.add(tf_last);
		
		ta = new JTextArea();
		ta.setBounds(93, 176, 198, 246);
		contentPane.add(ta);
		
		JButton btn = new JButton("별출력하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				showStar();
			}
		});
		btn.setBounds(140, 122, 97, 30);
		contentPane.add(btn);
	}

	protected void showStar() {
		
		int first = Integer.parseInt(tf_first.getText());
		int last = Integer.parseInt(tf_last.getText());
		
		String str = "";
		
		if(first > last) {
			ta.setText("첫별수가 끝별수보다 \n작게 입력해주세요");
		}else {
			for(int i = first; i < last+1; i++) {
				for(int k = 0; k < i; k++) {
					str += "*";
				}
				str += "\n";
			}
			ta.setText(str);
		}
	}
}
