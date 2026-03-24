import streamlit as st
import os
import shutil
import stat
from pathlib import Path

st.set_page_config(
    page_title="File & Folder Manager",
    page_icon="📁",
    layout="centered"
)

st.title("📁 File & Folder Management System")

BASE_PATH = Path.cwd().resolve()

def on_rm_error(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def safe_path(user_input):
    try:
        full_path = (BASE_PATH / user_input).resolve()
        full_path.relative_to(BASE_PATH)
        return full_path
    except:
        return None

def list_items():
    return list(BASE_PATH.rglob("*"))

menu = st.sidebar.radio(
    "Select Operation",
    (
        "Create Folder",
        "List Files & Folders",
        "Rename Folder",
        "Delete Folder",
        "Create File",
        "Read File",
        "Update File",
        "Delete File"
    )
)

if menu == "Create Folder":
    st.subheader("📂 Create Folder")
    folder_name = st.text_input("Enter folder name")
    if st.button("Create Folder"):
        p = safe_path(folder_name)
        if p:
            if not p.exists():
                p.mkdir(parents=True)
                st.success("Folder created successfully ✅")
                st.rerun()
            else:
                st.error("Folder already exists ❌")
        else:
            st.error("Invalid path ❌")

elif menu == "List Files & Folders":
    st.subheader("📃 Files & Folders List")
    items = list_items()
    if items:
        for i, item in enumerate(items, 1):
            icon = "📂" if item.is_dir() else "📄"
            st.write(f"{i}. {icon} {item.relative_to(BASE_PATH)}")
    else:
        st.info("No files or folders found")

elif menu == "Rename Folder":
    st.subheader("✏ Rename Folder")
    folders = [p.name for p in BASE_PATH.iterdir() if p.is_dir()]
    if folders:
        old_name = st.selectbox("Select folder", folders)
        new_name = st.text_input("Enter new folder name")
        if st.button("Rename Folder"):
            old_p = safe_path(old_name)
            new_p = safe_path(new_name)
            if old_p and new_p:
                if not new_p.exists():
                    old_p.rename(new_p)
                    st.success("Folder renamed successfully ✅")
                    st.rerun()
                else:
                    st.error("New folder already exists ❌")
            else:
                st.error("Invalid path ❌")
    else:
        st.info("No folders available")

elif menu == "Delete Folder":
    st.subheader("🗑 Delete Folder")
    folders = [p.name for p in BASE_PATH.iterdir() if p.is_dir()]
    if folders:
        name = st.selectbox("Select folder", folders)
        confirm = st.checkbox("Delete non-empty folder")
        if st.button("Delete Folder"):
            p = safe_path(name)
            if p and p.exists():
                try:
                    if confirm:
                        shutil.rmtree(p, onerror=on_rm_error)
                    else:
                        p.rmdir()
                    st.success("Folder deleted successfully ✅")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.error("Invalid path ❌")
    else:
        st.info("No folders available")

elif menu == "Create File":
    st.subheader("📄 Create File")
    file_name = st.text_input("Enter file name")
    content = st.text_area("File content")
    if st.button("Create File"):
        p = safe_path(file_name)
        if p:
            if not p.exists():
                p.write_text(content, encoding="utf-8")
                st.success("File created successfully ✅")
                st.rerun()
            else:
                st.error("File already exists ❌")
        else:
            st.error("Invalid path ❌")

elif menu == "Read File":
    st.subheader("📖 Read File")
    files = [p.name for p in BASE_PATH.iterdir() if p.is_file()]
    if files:
        name = st.selectbox("Select file", files)
        if st.button("Read File"):
            p = safe_path(name)
            if p:
                try:
                    content = p.read_text(encoding="utf-8")
                    st.code(content)
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.error("Invalid path ❌")
    else:
        st.info("No files available")

elif menu == "Update File":
    st.subheader("🛠 Update File")
    files = [p.name for p in BASE_PATH.iterdir() if p.is_file()]
    if files:
        name = st.selectbox("Select file", files)
        option = st.radio("Choose update type", ("Rename File", "Overwrite Content", "Append Content"))
        p = safe_path(name)
        if option == "Rename File":
            new_name = st.text_input("New file name")
            if st.button("Rename"):
                new_p = safe_path(new_name)
                if p and new_p:
                    if not new_p.exists():
                        p.rename(new_p)
                        st.success("File renamed successfully ✅")
                        st.rerun()
                    else:
                        st.error("File already exists ❌")
        elif option == "Overwrite Content":
            new_data = st.text_area("New content")
            confirm = st.checkbox("Confirm overwrite")
            if confirm and st.button("Overwrite"):
                if p:
                    p.write_text(new_data, encoding="utf-8")
                    st.success("File updated successfully ✅")
        elif option == "Append Content":
            append_data = st.text_area("Content to append")
            if st.button("Append"):
                if p:
                    with open(p, "a", encoding="utf-8") as f:
                        f.write("\n" + append_data)
                    st.success("Content appended successfully ✅")
    else:
        st.info("No files available")

elif menu == "Delete File":
    st.subheader("❌ Delete File")
    files = [p.name for p in BASE_PATH.iterdir() if p.is_file()]
    if files:
        name = st.selectbox("Select file", files)
        confirm = st.checkbox("Confirm delete")
        if confirm and st.button("Delete File"):
            p = safe_path(name)
            if p:
                try:
                    os.remove(p)
                    st.success("File deleted successfully ✅")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.error("Invalid path ❌")
    else:
        st.info("No files available")

st.markdown("---")
st.caption("🚀 Built with Python & Streamlit")