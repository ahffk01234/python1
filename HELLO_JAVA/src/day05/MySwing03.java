package day05;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.AbstractAction;
import java.awt.event.ActionEvent;
import javax.swing.Action;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class MySwing03 extends JFrame {

	private JPanel contentPane;
	private JTextField tfMine;
	private JTextField tfCom;
	private JTextField tfResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing03 frame = new MySwing03();
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
	public MySwing03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblMine = new JLabel("나 :");
		lblMine.setBounds(121, 75, 57, 15);
		contentPane.add(lblMine);
		
		JLabel lblCom = new JLabel("컴 :");
		lblCom.setBounds(121, 116, 57, 15);
		contentPane.add(lblCom);
		
		JLabel lblResult = new JLabel("결과 :");
		lblResult.setBounds(121, 161, 57, 15);
		contentPane.add(lblResult);
		
		tfMine = new JTextField();
		tfMine.setBounds(229, 72, 116, 21);
		contentPane.add(tfMine);
		tfMine.setColumns(10);
		
		tfCom = new JTextField();
		tfCom.setColumns(10);
		tfCom.setBounds(229, 113, 116, 21);
		contentPane.add(tfCom);
		
		JButton btn = new JButton("게임하기");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				String mine = tfMine.getText().trim();
				double db = Math.random();
				String com = "";
				String result = "";
				
				System.out.println(mine);
				
				if(db > 0.5) {
					com = "홀";
					tfCom.setText(com);
				}
				else {
					com = "짝";
					tfCom.setText(com);
				}
				
				System.out.println(com);
				
				if(mine.equals(com)) {
					result = "성공";
				}
				else {
					result ="실패";
				}
				tfResult.setText(result);
				System.out.println(result);
			}
		});
		btn.setBounds(167, 201, 97, 23);
		contentPane.add(btn);
		
		tfResult = new JTextField();
		tfResult.setBounds(229, 158, 116, 21);
		contentPane.add(tfResult);
		tfResult.setColumns(10);
	}
}
