class TestRoot:
    def test_read_root(self, client):
        response = client.get("/")
        assert response.status_code == 200
        expected = {
            "message": "Welcome to UrFU ML Engineering 2022, Group 20 project",
            "practice": "Practice 3 - Fast API",
            "git_hub": "https://github.com/urfuMagDS2022SFgroup/sf_data_science_python",
            "authors": [
                "Vladimir Katin <katin.v.v.@gmail.com>",
                "Anton Bessolitsyn <Anton.Bessolitsyn@hotmail.com>",
                "Alexander Orlov <eaglophone@gmail.com>",
                "Anna Bezhenar <asbezhenar@gmail.com>",
            ],
        }
        assert response.json() == expected
