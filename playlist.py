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

def view_playlist():
    """
    Hiển thị tất cả bài hát trong playlist
    Returns: Số lượng bài hát được hiển thị
    """
    print("\n" + "="*60)
    print("                   DANH SÁCH PLAYLIST")
    print("="*60)
    
    if not songs:
        print("📭 Playlist trống! Hãy thêm bài hát mới.")
        print("="*60)
        return 0
    
    # In header
    print(f"{'STT':<5} {'TÊN BÀI HÁT':<25} {'CA SĨ':<20} {'THỜI LƯỢNG':<10}")
    print("-"*60)
    
    # Duyệt và in từng bài hát
    for index, song in enumerate(songs, 1):
        # Format thời lượng từ giây -> phút:giây
        minutes = song['duration'] // 60
        seconds = song['duration'] % 60
        duration_formatted = f"{minutes}:{seconds:02d}"
        
        # In thông tin bài hát
        title = song['title'][:23] + "..." if len(song['title']) > 23 else song['title']
        artist = song['artist'][:18] + "..." if len(song['artist']) > 18 else song['artist']
        
        print(f"{index:<5} {title:<25} {artist:<20} {duration_formatted:<10}")
    
    print("="*60)
    
    # Tính tổng thời lượng
    total_seconds = sum(song['duration'] for song in songs)
    total_minutes = total_seconds // 60
    remaining_seconds = total_seconds % 60
    
    print(f"📊 Tổng số bài hát: {len(songs)}")
    print(f"⏱️  Tổng thời lượng: {total_minutes} phút {remaining_seconds} giây")
    print("="*60)
    
    return len(songs)

def search_by_artist():
    """
    Tìm kiếm bài hát theo tên ca sĩ
    Returns: Số lượng bài hát tìm thấy
    """
    print("\n" + "="*40)
    print("      TÌM BÀI HÁT THEO CA SĨ")
    print("="*40)
    
    if not songs:
        print("📭 Playlist trống! Hãy thêm bài hát mới.")
        return 0
    
    # Nhập tên ca sĩ cần tìm
    artist_name = input("Nhập tên ca sĩ cần tìm: ").strip().lower()
    
    if not artist_name:
        print("❌ Vui lòng nhập tên ca sĩ!")
        return 0
    
    # Tìm bài hát
    found_songs = []
    for song in songs:
        if artist_name in song['artist'].lower():
            found_songs.append(song)
    
    # Hiển thị kết quả
    print("\n" + "="*60)
    print(f"   KẾT QUẢ TÌM KIẾM: '{artist_name.upper()}'")
    print("="*60)
    
    if not found_songs:
        print(f"❌ Không tìm thấy bài hát của ca sĩ '{artist_name}'")
        print("="*60)
        return 0
    
    print(f"🎵 Tìm thấy {len(found_songs)} bài hát:")
    print("-"*60)
    print(f"{'STT':<5} {'TÊN BÀI HÁT':<25} {'THỜI LƯỢNG':<10}")
    print("-"*60)
    
    for index, song in enumerate(found_songs, 1):
        minutes = song['duration'] // 60
        seconds = song['duration'] % 60
        duration_formatted = f"{minutes}:{seconds:02d}"
        
        title = song['title'][:23] + "..." if len(song['title']) > 23 else song['title']
        print(f"{index:<5} {title:<25} {duration_formatted:<10}")
    
    print("="*60)
    return len(found_songs)

if __name__ == "__main__":
    main()
elif choice == "2":
    # Gọi hàm xem playlist
    view_playlist()
    input("\nNhấn Enter để tiếp tục...")