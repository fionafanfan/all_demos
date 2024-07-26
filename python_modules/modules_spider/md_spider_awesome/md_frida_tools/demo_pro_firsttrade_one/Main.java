import javax.crypto.Cipher;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.PBEParameterSpec;
import java.security.spec.KeySpec;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        // ����
        char[] password = "771589S".toCharArray();
        // �Σ�16�����ַ���ת��Ϊ�ֽ����飩
        byte[] salt = new byte[]{(byte) 0x2a, (byte) 0xe3, (byte) 0x01, (byte) 0xee, (byte) 0x68, (byte) 0x6c, (byte) 0x69, (byte) 0x15};
        // ��������
        int iterationCount = 1000;
        // ��Կ����
        int keyLength = 64;

        // ����PBEKeySpec
        KeySpec keySpec = new PBEKeySpec(password, salt, iterationCount, keyLength);
        // ����SecretKeyFactory
        SecretKeyFactory keyFactory = SecretKeyFactory.getInstance("PBEwithMD5andDES");
        // ������Կ
        javax.crypto.SecretKey secretKey = keyFactory.generateSecret(keySpec);

        // ����PBEParameterSpec
        PBEParameterSpec parameterSpec = new PBEParameterSpec(salt, iterationCount);

        // ����Cipherʵ������ʼ��Ϊ����ģʽ
        Cipher cipher = Cipher.getInstance("PBEwithMD5andDES");
        cipher.init(Cipher.DECRYPT_MODE, secretKey, parameterSpec);

        // ���ܺ������
        byte[] encryptedData = new byte[]{(byte) -13, (byte) -27, (byte) 93, (byte) 93, (byte) 24, (byte) -55, (byte) 81, (byte) -76};

        // ��������
        byte[] decryptedData = cipher.doFinal(encryptedData);

        // ��ӡ���ܽ��
        System.out.println("Decrypted Data: " + Arrays.toString(decryptedData));
        System.out.println("Decrypted String: " + new String(decryptedData));
    }
}

// ����java����: https://www.bejson.com/runcode/java/
// ����java����ִ��������:
// Decrypted Data: [71, 114, 56, 57, 76, 77]
// Decrypted String: Gr89LM

