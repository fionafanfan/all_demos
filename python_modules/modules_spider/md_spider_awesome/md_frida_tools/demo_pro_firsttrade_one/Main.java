import javax.crypto.Cipher;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.PBEParameterSpec;
import java.security.spec.KeySpec;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        // 密码
        char[] password = "771589S".toCharArray();
        // 盐（16进制字符串转换为字节数组）
        byte[] salt = new byte[]{(byte) 0x2a, (byte) 0xe3, (byte) 0x01, (byte) 0xee, (byte) 0x68, (byte) 0x6c, (byte) 0x69, (byte) 0x15};
        // 迭代次数
        int iterationCount = 1000;
        // 密钥长度
        int keyLength = 64;

        // 创建PBEKeySpec
        KeySpec keySpec = new PBEKeySpec(password, salt, iterationCount, keyLength);
        // 创建SecretKeyFactory
        SecretKeyFactory keyFactory = SecretKeyFactory.getInstance("PBEwithMD5andDES");
        // 生成密钥
        javax.crypto.SecretKey secretKey = keyFactory.generateSecret(keySpec);

        // 创建PBEParameterSpec
        PBEParameterSpec parameterSpec = new PBEParameterSpec(salt, iterationCount);

        // 创建Cipher实例并初始化为解密模式
        Cipher cipher = Cipher.getInstance("PBEwithMD5andDES");
        cipher.init(Cipher.DECRYPT_MODE, secretKey, parameterSpec);

        // 加密后的数据
        byte[] encryptedData = new byte[]{(byte) -13, (byte) -27, (byte) 93, (byte) 93, (byte) 24, (byte) -55, (byte) 81, (byte) -76};

        // 解密数据
        byte[] decryptedData = cipher.doFinal(encryptedData);

        // 打印解密结果
        System.out.println("Decrypted Data: " + Arrays.toString(decryptedData));
        System.out.println("Decrypted String: " + new String(decryptedData));
    }
}

// 在线java环境: https://www.bejson.com/runcode/java/
// 在线java环境执行输出结果:
// Decrypted Data: [71, 114, 56, 57, 76, 77]
// Decrypted String: Gr89LM

