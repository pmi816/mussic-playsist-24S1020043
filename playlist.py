songs = []
def add_song():
    """
    Thêm bài hát mới vào playlist
    Returns: True nếu thành công, False nếu thất bại
    """
    print("\n" + "="*40)
    print("      THÊM BÀI HÁT MỚI")
    print("="*40)
    
    try:
        # Nhập tên bài hát
        title = input("Nhập tên bài hát: ").strip()
        if not title:
            print("❌ Tên bài hát không được để trống!")
            return False
        
        # Nhập tên ca sĩ
        artist = input("Nhập tên ca sĩ/nhóm nhạc: ").strip()
        if not artist:
            print("❌ Tên ca sĩ không được để trống!")
            return False
        
        # Nhập và kiểm tra thời lượng
        while True:
            duration_str = input("Nhập thời lượng (giây): ").strip()
            try:
                duration = int(duration_str)
                if duration <= 0:
                    print("❌ Thời lượng phải lớn hơn 0 giây!")
                    continue
                break
            except ValueError:
                print("❌ Vui lòng nhập số nguyên dương!")
        
        # Tạo dictionary lưu thông tin bài hát
        song = {
            'title': title,
            'artist': artist,
            'duration': duration
        }
        
        # Thêm vào danh sách
        songs.append(song)
        
        print(f"\n✅ Đã thêm bài hát thành công!")
        print(f"   🎵 Tên bài hát: {title}")
        print(f"   🎤 Ca sĩ: {artist}")
        print(f"   ⏱️ Thời lượng: {duration} giây")
        print(f"\n📊 Tổng số bài hát trong playlist: {len(songs)}")
        return True
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Đã hủy thao tác thêm bài hát!")
        return False
    except Exception as e:
        print(f"\n❌ Lỗi khi thêm bài hát: {e}")
        return False

def main():
    while True:
        print("\n=== PLAYLIST MANAGER ===")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Thoát")
        
        choice = input("Chọn chức năng: ")
        
        if choice == "1":
            print("Tính năng đang phát triển...")
        elif choice == "2":
            print("Tính năng đang phát triển...")
        elif choice == "3":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()