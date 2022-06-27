# Recursive GNU Make wildcard implementation
# https://stackoverflow.com/questions/2483182/recursive-wildcards-in-gnu-make/18258352#18258352
rwildcard=$(foreach d,$(wildcard $(1:=/*)),$(call rwildcard,$d,$2) $(filter $(subst *,%,$2),$d))


run:  ## [Local development] Run human tracking on the full video
	python src/main.py -i input_videos/miss_dior.mp4 -m yolo -s flash

run-small: ## [Local development] Run human tracking on the small video
	python src/main.py -i input_videos/miss_dior_small.mp4 -m yolo -s flash

run-hd: ## [Local development] Run human tracking on the full HD video
	python src/main.py -i input_videos/miss_dior_hd.mp4 -m yolo -s flash

format: ## [Local development] Auto-format python code using black
	black src

run-demo:  ## [Local development] Run demo app
	streamlit run app.py

install: ## [Local development] Install packages
	conda create --name aive python=3.9
	conda install --force-reinstall -y -q --name aive  -c conda-forge --file requirements.txt
	conda activate aive