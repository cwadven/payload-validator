## 1. Git Hooks

- flake8 running before commit
- check branch name
- add prefix-branch-name in commit message

make sure to check if git hooks are linked

### 1. Go to git hooks directory 

```shell
cd .git/hooks
```

### 2. Link git-hooks

check if payload-validator/git-hooks directory well setup

```shell
for hook_path in ~/MyProject/payload-validator/git-hooks/*
do
  if [ "${hook_path##*.}" != "py" ]  # Ignore .py files
  then
    ln -s "$hook_path" .
  fi
done
```

### 3. Check if git hooks are linked

```shell
ls -alth
```

Linux

```shell
total 120
drwxr-xr-x  18 a202205037  42747544   576B  7 23 13:22 .
lrwxr-xr-x   1 a202205037  42747544    76B  7 23 13:22 prepare-commit-msg -> /workspace/payload-validator/pre-commits/prepare-commit-msg
lrwxr-xr-x   1 a202205037  42747544    68B  7 23 13:22 pre-commit -> /workspace/payload-validator/pre-commits/pre-commit
lrwxr-xr-x   1 a202205037  42747544    68B  7 23 13:22 commit-msg -> /workspace/payload-validator/pre-commits/commit-msg
drwxr-xr-x  13 a202205037  42747544   416B  7 23 12:22 ..
-rwxr-xr-x   1 a202205037  42747544   2.7K  7 23 12:22 push-to-checkout.sample
-rwxr-xr-x   1 a202205037  42747544   3.6K  7 23 12:22 update.sample
-rwxr-xr-x   1 a202205037  42747544   1.3K  7 23 12:22 pre-push.sample
-rwxr-xr-x   1 a202205037  42747544   424B  7 23 12:22 pre-applypatch.sample
-rwxr-xr-x   1 a202205037  42747544   416B  7 23 12:22 pre-merge-commit.sample
-rwxr-xr-x   1 a202205037  42747544   189B  7 23 12:22 post-update.sample
-rwxr-xr-x   1 a202205037  42747544   1.5K  7 23 12:22 prepare-commit-msg.sample
-rwxr-xr-x   1 a202205037  42747544   544B  7 23 12:22 pre-receive.sample
-rwxr-xr-x   1 a202205037  42747544   4.5K  7 23 12:22 fsmonitor-watchman.sample
-rwxr-xr-x   1 a202205037  42747544   478B  7 23 12:22 applypatch-msg.sample
-rwxr-xr-x   1 a202205037  42747544   1.6K  7 23 12:22 pre-commit.sample
-rwxr-xr-x   1 a202205037  42747544   4.8K  7 23 12:22 pre-rebase.sample
-rwxr-xr-x   1 a202205037  42747544   896B  7 23 12:22 commit-msg.sample
```

Windows added file

```shell
ls -al
```

```shell
drwxr-xr-x 1 Sedragon 197121    0 Jul 23 14:17 .
drwxr-xr-x 1 Sedragon 197121    0 Jul 23 14:18 ..
-rwxr-xr-x 1 Sedragon 197121  478 Jul 23 14:08 applypatch-msg.sample
-rwxr-xr-x 1 Sedragon 197121 1589 Jul 23 14:13 commit-msg
-rwxr-xr-x 1 Sedragon 197121  896 Jul 23 14:08 commit-msg.sample
-rwxr-xr-x 1 Sedragon 197121 4726 Jul 23 14:08 fsmonitor-watchman.sample
-rwxr-xr-x 1 Sedragon 197121  189 Jul 23 14:08 post-update.sample
-rwxr-xr-x 1 Sedragon 197121  424 Jul 23 14:08 pre-applypatch.sample
-rwxr-xr-x 1 Sedragon 197121  280 Jul 23 14:11 pre-commit
-rwxr-xr-x 1 Sedragon 197121 1643 Jul 23 14:08 pre-commit.sample
-rwxr-xr-x 1 Sedragon 197121  416 Jul 23 14:08 pre-merge-commit.sample
-rwxr-xr-x 1 Sedragon 197121 1374 Jul 23 14:08 pre-push.sample
-rwxr-xr-x 1 Sedragon 197121 4898 Jul 23 14:08 pre-rebase.sample
-rwxr-xr-x 1 Sedragon 197121  544 Jul 23 14:08 pre-receive.sample
-rwxr-xr-x 1 Sedragon 197121 3330 Jul 23 14:13 prepare-commit-msg
-rwxr-xr-x 1 Sedragon 197121 1492 Jul 23 14:08 prepare-commit-msg.sample
-rwxr-xr-x 1 Sedragon 197121 2783 Jul 23 14:08 push-to-checkout.sample
-rwxr-xr-x 1 Sedragon 197121 3650 Jul 23 14:08 update.sample
```


### 4. Add using permissions

```shell
chmod +x pre-commit
chmod +x prepare-commit-msg
chmod +x commit-msg
```