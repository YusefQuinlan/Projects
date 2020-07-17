package NotepadWrite;
import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.InputEvent;
import java.awt.event.KeyEvent;
import java.io.*;
import java.io.IOException;

public class Main1 {

	public static void main(String[] args) throws IOException,
	AWTException, InterruptedException
	{
		// TODO Auto-generated method stub
		String command = "notepad.exe";
		Runtime run = Runtime.getRuntime();
		run.exec(command);
		// Try catch statement for errors.
		try {
			Thread.sleep(2000);
		}
		catch (InterruptedException e)
		{
			e.printStackTrace();
		}
		// creating a new robot
		Robot robot = new Robot();
		
		//press keys using robot inside of notepad (via run)
		// 500 millisecond breaks between presses
		// exiting notepad will break this bot and the bot
		// will press these keys but outside of notepad.
		robot.keyPress(KeyEvent.VK_CAPS_LOCK);
		robot.keyRelease(KeyEvent.VK_CAPS_LOCK);
		robot.keyPress(KeyEvent.VK_Y);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_CAPS_LOCK);
		robot.keyRelease(KeyEvent.VK_CAPS_LOCK);
		robot.keyPress(KeyEvent.VK_U);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_S);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_E);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_F);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_SPACE);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_CAPS_LOCK);
		robot.keyRelease(KeyEvent.VK_CAPS_LOCK);
		robot.keyPress(KeyEvent.VK_Q);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_CAPS_LOCK);
		robot.keyRelease(KeyEvent.VK_CAPS_LOCK);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_U);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_I);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_N);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_L);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_A);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_N);
		Thread.sleep(50);
		robot.keyPress(KeyEvent.VK_PERIOD);
		
		command = "mspaint.exe";
		run.exec(command);
		Thread.sleep(4500);
		robot.mouseMove(30,160);
		robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
		robot.mouseMove(60, 190);
		Thread.sleep(100);
		robot.mouseMove(60, 250);
		Thread.sleep(100);
		robot.mouseMove(60, 190);
		Thread.sleep(100);
		robot.mouseMove(90, 160);
		//start u
		robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(120, 160);
		robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(120, 250);
		Thread.sleep(100);
		robot.mouseMove(180, 250);
		Thread.sleep(100);
		robot.mouseMove(180, 160);
		Thread.sleep(100);
		//start s
		robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
		robot.mouseMove(210, 160);
		robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(270, 160);
		Thread.sleep(100);
		robot.mouseMove(210, 160);
		Thread.sleep(100);
		robot.mouseMove(210, 205);
		Thread.sleep(100);
		robot.mouseMove(270, 205);
		Thread.sleep(100);
		robot.mouseMove(270, 250);
		Thread.sleep(100);
		robot.mouseMove(210, 250);
		Thread.sleep(100);
		//start e
		robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
		robot.mouseMove(300, 160);
		robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(360, 160);
		Thread.sleep(100);
		robot.mouseMove(300, 160);
		Thread.sleep(100);
		robot.mouseMove(300, 205);
		Thread.sleep(100);
		robot.mouseMove(360, 205);
		Thread.sleep(100);
		robot.mouseMove(300, 205);
		Thread.sleep(100);
		robot.mouseMove(300, 250);
		Thread.sleep(100);
		robot.mouseMove(360, 250);
		Thread.sleep(100);
		// Start F
		robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
		robot.mouseMove(390,160);
		robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(450, 160);
		Thread.sleep(100);
		robot.mouseMove(390,160);
		Thread.sleep(100);
		robot.mouseMove(390, 205);
		Thread.sleep(100);
		robot.mouseMove(450, 205);
		Thread.sleep(100);
		robot.mouseMove(390, 205);
		Thread.sleep(100);
		robot.mouseMove(390, 250);
		Thread.sleep(100);
		
		//move down and start q
		robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
		robot.mouseMove(30, 300);
		robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(30, 390);
		Thread.sleep(100);
		robot.mouseMove(30, 300);
		Thread.sleep(100);
		robot.mouseMove(90, 300);
		Thread.sleep(100);
		robot.mouseMove(90, 390);
		Thread.sleep(100);
		robot.mouseMove(30, 390);
		Thread.sleep(100);
		robot.mouseMove(60, 390);
		Thread.sleep(100);
		robot.mouseMove(60, 430);
		Thread.sleep(100);
		
		//start u
		robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(120, 300);
		robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(120, 390);
		Thread.sleep(100);
		robot.mouseMove(180, 390);
		Thread.sleep(100);
		robot.mouseMove(180, 300);
		Thread.sleep(100);
		
		//start I
		robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(210, 300);
		robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(270, 300);
		Thread.sleep(100);
		robot.mouseMove(240, 300);
		Thread.sleep(100);
		robot.mouseMove(240, 390);
		Thread.sleep(100);
		robot.mouseMove(270, 390);
		Thread.sleep(100);
		robot.mouseMove(210, 390);
		Thread.sleep(100);
		
		//Start N
		robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
		robot.mouseMove(300, 300);
		robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(300, 390);
		Thread.sleep(100);
		robot.mouseMove(300, 300);
		Thread.sleep(100);
		robot.mouseMove(360, 390);
		Thread.sleep(100);
		robot.mouseMove(360, 300);
		Thread.sleep(100);
		
		//Start L
		robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
		robot.mouseMove(390, 300);
		robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(390, 390);
		Thread.sleep(100);
		robot.mouseMove(450, 390);
		Thread.sleep(100);
		
		//Start A
		robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
		robot.mouseMove(510, 300);
		robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(480, 390);
		Thread.sleep(100);
		robot.mouseMove(510, 300);
		Thread.sleep(100);
		robot.mouseMove(540, 390);
		Thread.sleep(100);
		robot.mouseMove(525, 345);
		Thread.sleep(100);
		robot.mouseMove(495, 345);
		Thread.sleep(100);
		
		//Start N
		robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
		robot.mouseMove(570, 300);
		robot.mousePress(InputEvent.BUTTON1_DOWN_MASK);
		Thread.sleep(100);
		robot.mouseMove(570, 390);
		Thread.sleep(100);
		robot.mouseMove(570, 300);
		Thread.sleep(100);
		robot.mouseMove(630, 390);
		Thread.sleep(100);
		robot.mouseMove(630, 300);
		Thread.sleep(100);
		robot.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
		
	}

}
