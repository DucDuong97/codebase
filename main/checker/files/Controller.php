<?php

	namespace app\core;

	class Controller {

		const CSRF_TOKEN_LENGTH = 32;

		/**
		 * Render view content
		 * @return string
		 */
		protected function renderView($view,$params = [] ) {
			// Get layout content
			ob_start();
			$app = Application::$app;
			include_once Application::$ROOT_DIR."/views/_layout.php";
			$layout_content = ob_get_clean();

			// Get view content
			foreach ($params as $key => $value) {
				$$key = $value;
			}
			ob_start();
			include_once Application::$ROOT_DIR."/views/$view.php";
			$view_content = ob_get_clean();

			// Replace view content in layout placeholder
			$content = str_replace('{{content}}', $view_content, $layout_content);

			return $content;
		}

		/**
		 * Generate CSRF token
		 * @param string Token key
		 * @return string
		 */
		protected function generateCsrfToken($key) {
			$session = Application::$app->getSession();
			$token = bin2hex(random_bytes(static::CSRF_TOKEN_LENGTH));
			$session->set($key, $token);
			return $token;
		}

		 /**
		 * Get CSRF token
		 * @param string Token key
		 * @return string
		 */
		protected function getCsrfToken($key) {
			$session = Application::$app->getSession();
			$token = $session->get($key);
			return $token;
		}

		/**
		 * if()
		 * Validate CSRF token
		 * @param string Token key
		 * @param string Token value
		 * @return boolean
		 */
		protected function validateCsrfToken($key) {
			$session = Application::$app->getSession();
			$csrf_Token = $session->get($key) ;
			if  (empty($_POST[$key])) {
				return $csrf_Token == $_POST[$key];
			}
			return false;
		}
	}

?>